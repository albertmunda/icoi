#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/*
 @AUTHOR----> DHWAJ VERMA
*/

struct node
{
	double x;
	double y;
	double centx;
	double centy;
	double distance;
	int k;
	struct node *next;
	struct node *reps;
};


// function declartions
struct node* createNode1(double x,double y);
struct node* makeSet(double x,double y,struct node *node);
struct node* makeGlobalSet(FILE *f,struct node *node);
void printSet(struct node *node,int n);
int countSet(struct node *node);
double calcDistance(struct node *node1,struct node *node2);
void setCenteroid(struct node *node);
struct node* deleteAtK(struct node *node,int k);
struct node* findMinNode(struct node *node2,int n);
struct node* calcDistanceArray(struct node *node1,struct node* node2);
struct node* makeCluster(struct node *node1,struct node *node2,int k);
struct node* makeCluster2(struct node *node1,struct node *node2,int k);
FILE* printFile(struct node *node,FILE *f);



// create node
struct node* createNode1(double x,double y)
{
	struct node *temp=(struct node* ) malloc(sizeof(struct node));
	temp->x=x;
	temp->y=y;
	temp->centx=0;
	temp->centy=0;
	temp->distance=0;
	temp->next=NULL;
	return temp;
}

// its make set 
struct node* makeSet(double x,double y,struct node *node)
{
	struct node *temp=node;
	if(node==NULL)
	{
		struct node *node2=createNode1(x,y);
		node2->reps=node2;
		return node2;
	}
	else
	{
		struct node *temp1=createNode1(x,y);
		while(temp->next!=NULL)
		{
			temp=temp->next;
		}
		temp1->reps=node;
		temp->next=temp1;
		return node;
	}
}


// makes the global set
struct node* makeGlobalSet(FILE *f,struct node *node)
{
	char str[999];
    struct node *head=node;
	if (f)
	{
		while(fscanf(f,"%[^\n]\n",str)!=EOF)
		{
			char *p=strtok(str,"\t");
			double x=0;
			double y=0;
			sscanf(p,"%lf",&x);
			p=strtok(NULL,"\t");
			sscanf(p,"%lf",&y);
			head=makeSet(x,y,head);
		}
		fclose(f);
	}
	return head;
}

// prints the set
void printSet(struct node *node,int n)
{
	int i=0;
	struct node *temp=node;
	while(temp!=NULL && i <= n-1)
	{
		printf("{ \n");
		printf("x=%lf y=%lf\n",temp->x,temp->y);
		printf("centx=%lf centy=%lf \n",temp->centx,temp->centy);
		printf("distance==%lf\n",temp->distance);
		printf("}\n");
		i++;
		temp=temp->next;
	}
}

//counts the set
int countSet(struct node *node)
{
	int count=0;
	struct node *temp=node;
	while(temp!=NULL)
	{
		temp=temp->next;
		count++;
	}
	return count;	
}

//calclulates distance
double calcDistance(struct node *node1,struct node *node2)
{
	//printf("calcDistance runs\n");
	double x1=node1->centx,y1=node1->centy,x2=node2->x,y2=node2->y;
	double distance=0.00;
    distance=sqrt( pow((x2-x1),2) + pow((y2-y1),2) );
    return distance;
}

// sets the cetroid for that set
void setCenteroid(struct node *node)
{
	//printf("setCenteroid runs with node->x==%lf\n",node->x);
	struct node *temp=node;
	double centx=0,centy=0;
	int n=countSet(node);
	//printf("count of set ==%d\n",n);
	while(temp!=NULL)
	{
		centx=centx+temp->x;
		centy=centy+temp->y;
		temp=temp->next;
	}
	//printf("centx==%lf centy==%lf \n",centx,centy);
	centx=centx/n;
	centy=centy/n;
    //printf("centx= %lf centy=%lf \n",centx,centy);
	node->centx=centx;
	node->centy=centy;
	return;
}

// finds the min of list
struct node* findMinNode(struct node *node2,int n)
{
	struct node *temp1=NULL;
	struct node *temp2=node2;
	struct node *temp5=NULL;
	int i=0,k=0;
	double min=temp2->next->distance;
	temp2=temp2->next;
	while(temp2!=NULL && i < n)
	{
		if(temp2->distance < min)
		{
			min=temp2->distance;
			temp1=temp2;
			k=i;
		}
		temp2=temp2->next;
		i++;
	}
	temp1->k=k;
	return temp1;
}


// deletes the node at k distance
struct node* deleteAtK(struct node *node,int k)
{
	int i=0;
	struct node *temp3=node;
	struct node *temp4=temp3->next;
	while(i <= k-1 && temp4!=NULL)
	{
		temp3=temp3->next;
		temp4=temp4->next;
		i++;		
	}
	temp3->next=temp4->next;
	return node;
}

// fills the first 500 pts distance from that point
struct node* calcDistanceArray(struct node *node1,struct node* node2)
{
	struct node *set1=node1;
	struct node *set2=node2;
	setCenteroid(set1);
	int i=0;
	while(set2!=NULL && i < 500)
	{
		double dis=calcDistance(set1,set2);
		set2->distance=dis;
		set2=set2->next;
		i++;
	}
	return  node2;
}

// makes the cluster
struct node* makeCluster(struct node *node1,struct node *node2,int k)
{
	//printf("makeCluster runs\n");
	int i=0;
	struct node *temp1=node1;
	struct node *temp2=node2;
    node1=makeSet(node2->x,node2->y,node1);
	for (i=0;i<=k-1;i++)
	{
		node2=calcDistanceArray(node1,node2);
		struct node *min=findMinNode(node2,500);
		node1=makeSet(min->x,min->y,node1);
		node2=deleteAtK(node2,min->k);
    }
 	return node1;
 }

// makes the cluster
struct node* makeCluster2(struct node *node1,struct node *node2,int k)
{
   	//printf("makeCluster 2 runs\n");
	int i=0;
	struct node *temp1=node1;
	struct node *temp2=node2;
	while(i<=503)
	{
		temp2=temp2->next;
		i++;
	}
    node1=makeSet(node2->x,node2->y,node1);
	for (i=0;i<=k-1;i++)
	{
		if(i <= countSet(temp2)-2)
	    {
			node2=calcDistanceArray(node1,node2);
			struct node *min=findMinNode(node2,500);
			node1=makeSet(min->x,min->y,node1);
			node2=deleteAtK(node2,min->k);
    	}
    }
 	
 	return node1;
}

// it will put the cluster in file for plotting
FILE* printFile(struct node *node,FILE *f)
nx{
	struct node *temp=node;
	if (f==NULL)
	{
		printf("Error!");
	}
	else
	{
		fprintf(f, "#  X\t\tY\n");
		while(temp!=NULL)
		{
			fprintf(f, "   %lf\t",temp->x);
			fprintf(f, "%lf\n",temp->y);
			temp=temp->next;
		}
	}
	return f;
}


// main
int main()
{
	printf("Wait for 1 min till global set forms .... \n");
	int k=0,total=0,threshold=0,i=0;
	struct node *globalhead=NULL;
	FILE *f=fopen("sample2.txt","r");
	globalhead=makeGlobalSet(f,globalhead);
	printf("enter the value of k which is *****( K > 0)*****\n");
	scanf("%d",&k);
    struct node* arr[k];
    FILE* farr[k];
    for(i=0;i<=k-1;i++)
    {
    	char filename[10];
    	sprintf (filename, "cluster_%d.dat", i);
 		farr[i]=fopen(filename,"w");	
    }
    for(i=0;i<=k-1;i++)
    {
    	arr[i]=NULL;
    }
    total=countSet(globalhead);
    threshold=total/k;
    for(i=0;i<=k-1;i++)
    {
    	if(i==0)
    	{
    		printf("cluster_0 is forming...\n");
    		arr[i]=makeCluster(arr[i],globalhead,threshold);
    		farr[i]=printFile(arr[i],farr[i]);
    		printf("cluster_0 is formed...\n");
    	}
    	else
    	{
    		printf("cluster_%d is forming...\n",i);
    		arr[i]=makeCluster2(arr[i],globalhead,threshold);
    		farr[i]=printFile(arr[i],farr[i]);
    		printf("cluster_%d is formed...\n",i);
    	}
    }
    printf("*******************ALL CLUSTERS FORMED***********************\n");
    return 0;
}


