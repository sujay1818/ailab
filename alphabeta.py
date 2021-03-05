import math

MAX,MIN=1000,-1000

def minimax(curdepth,nodeindex,maxplayer,nodes,targetdepth,alpha,beta):
	
	if(curdepth==targetdepth):
		return nodes[nodeindex]
	
	if(maxplayer):
		
		best=MIN
			
		for i in range(0,2):
			val=minimax(curdepth+1, nodeindex*2+i, False, nodes, targetdepth, alpha, beta)
			
			best= max(best,val)
			alpha= max(alpha,best)
			
			if alpha<=beta :
				break
			
		return best
			
	else:
	
		best=MAX
		
		for i in range(0,2):
		
			val=minimax(curdepth+1, nodeindex*2+i, True, nodes, targetdepth, alpha, beta)
			
			best= min(best,val)
			alpha= max(beta,best)
			
			if alpha<=beta:
				break
			
		return best

nodes=[]
print('Enter the length of the array')
size=int(input())
print('Enter the elements')
for i in range(int(size)):
	k=int(input(""))
	k=nodes.append(k)
	
treedepth = math.log(len(nodes),2)

print('The optimal solution is ')
print(minimax(0,0,True,nodes,treedepth,MAX,MIN))

		
