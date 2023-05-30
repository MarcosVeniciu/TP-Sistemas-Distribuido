/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/cFiles/main.c to edit this template
 */

/* 
 * File:   main.c
 * Author: thais
 *
 * Created on 10 de junho de 2022, 10:58
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>
#include <unistd.h>

#define SERVER_PORT 7896
#define MAX_PENDING 5
#define MAX_LINE 1024

/*
 * 
 */
int main(int argc, char** argv) {
    
    struct sockaddr_in sin;
    char buf[MAX_LINE] = {0};
    int len;
    int s, new_s;
    char* hello = "PONG!!!";
        
    /*Constrói estrutura de dados de endereço*/
    memset(&sin,0,sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = htonl(INADDR_ANY);
    sin.sin_port = htons(SERVER_PORT);
    
    if((s = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        perror("simplex-talk: socket");
        exit(1);
    }
    
    if((bind(s,(struct sockaddr*)&sin,sizeof(sin))) < 0){
        perror("simplex-talk: bind");
        exit(1);
    }
    
    listen(s, MAX_PENDING);
    
    
    while(1){
        printf("Esperando...\n"); 
        
        if((new_s = accept(s,(struct sockaddr*)&sin,&len)) < 0){
            perror("simplex-talk: accept");
            exit(1);
        }
        printf("Atendendo Cliente!\n");
                
        len = recv(new_s, buf, MAX_LINE, 0);        
        
        printf("%s\n",buf);
        
        send(new_s,hello,strlen(hello),0);
        
        printf("PONG!!!\n");
        
        close(new_s);  
    }
    
    return (EXIT_SUCCESS);
}

