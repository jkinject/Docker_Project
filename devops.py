import sys
import os
import time

def start():
    os.system('docker-compose up -d')

def stop():
    os.system('docker-compose stop')

def restart():
    os.system('docker-compose restart')

def deploy():
    #build
    os.system('webserver/sample-web-ui/gradlew build -x test -p webserver/sample-web-ui/')
    os.system('docker-compose build')

    #get conf
    fpath = "nginx/nginx.conf"
    servers = 0
    lines = []
    with open(fpath, 'r') as f:
        for line in f:
            if line.startswith('    server '):
                lines.insert(servers, line)
                servers += 1
            elif line.startswith('#    server '):
                lines.insert(servers, line)
                servers += 1

    print("Total Server Count : %d" %(servers))
    os.system('cp nginx/nginx.conf nginx/nginx.conf_org')

    #deployment
    for c in range(0, servers):
        with open(fpath, "r+w") as f:
            data = f.readlines()
            f.seek(0)

            i = 0
            for line in data:
                if line.startswith('    server '):
                    data[i] = line.replace(lines[c], '#%s' % (lines[c]))

                elif line.startswith('#    server '):
                    data[i] = line.replace('#', "")

                f.write(data[i])
                i += 1

        print('%d webserver deploy Start' % (c+1))
        #os.system('cat nginx/nginx.conf')
        deploy_conf()
        
        #os.system('docker kill webserver%d' % (c+1))
        os.system('docker-compose up -d webserver%d' % (c+1))

        # TODO: WEBSERVER HEALTH CHECK
        time.sleep(15)
        print('%d webserver deploy Completed' % (c+1))

    #complete
    os.system('cp nginx/nginx.conf_org nginx/nginx.conf')
    deploy_conf()

def deploy_conf():
    print('Copy nginx.conf file')
    os.system('docker cp nginx/nginx.conf lb:/etc/nginx/conf.d/default.conf')
    time.sleep(1)
    print('nginx reload')
    os.system('docker exec lb nginx -s reload')

def show_help():
    print("\nUsage:\n\tpython devops.py [start | stop | restart | deploy]\n\n")

if __name__ == "__main__":
    # Get parameter
    if len(sys.argv) is 1:
        show_help()
        sys.exit(1)

    command = sys.argv[1]

    if "start" == command:
        start()
    elif "stop" == command:
        stop()
    elif "restart" == command:
        restart()
    elif "deploy" == command:
        deploy()
    else:
        show_help()

