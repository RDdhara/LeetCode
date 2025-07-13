import java.util.Arrays;
class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        int m = players.length;
        int n = trainers.length;

        Arrays.sort(players);
        Arrays.sort(trainers);

        int i = 0, j = 0;
        int count = 0;

        while(i < m && j < n){
            if(players[i] > trainers[j]){
                j++;
            }
            else{
                count++;
                i++;
                j++;
            }
        }
        return count;
    }
}
