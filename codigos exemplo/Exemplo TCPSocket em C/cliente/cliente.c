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
    int s;
    char* txt = "PING!!!";
        
    /*Constrói estrutura de dados de endereço*/
    memset(&sin,0,sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = htonl(INADDR_ANY);
    sin.sin_port = htons(SERVER_PORT);
    
    if((s = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        perror("simplex-talk: socket");
        exit(1);
    }
    
    if((connect(s,(struct sockaddr*)&sin,sizeof(sin))) < 0){
        perror("simplex-talk: connect");
        exit(1);
    }
    
    printf("Enviando...\n"); 
        
    send(s,txt,strlen(txt),0);
    
    printf("PING!!!\n");
        
    len = recv(s, buf, MAX_LINE, 0);        
        
    printf("%s\n",buf);
        
    close(s);  
 
    return (EXIT_SUCCESS);
}

