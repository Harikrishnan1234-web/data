public class DistanceVector {
    public static void main(String[] args) {
        int INF = 999;
        int[][] graph = {{0,1,4},{1,0,2},{4,2,0}};
        int[] distance = {0, INF, INF};

        for(int k=0;k<graph.length;k++) {
            for(int i=0;i<graph.length;i++) {
                for(int j=0;j<graph.length;j++) {
                    if(distance[j] > distance[i] + graph[i][j])
                        distance[j] = distance[i] + graph[i][j];
                }
            }
        }

        for(int i=0;i<distance.length;i++)
            System.out.println("Distance to " + i + " = " + distance[i]);
    }
}