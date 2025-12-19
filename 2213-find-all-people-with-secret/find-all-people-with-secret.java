import java.util.*;

class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        // Sort meetings by time
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[2], b[2]));
        
        // Track who knows the secret
        boolean[] knowsSecret = new boolean[n];
        knowsSecret[0] = true;
        knowsSecret[firstPerson] = true;
        
        int m = meetings.length;
        int i = 0;
        
        while (i < m) {
            int time = meetings[i][2];
            
            // Build graph for this time slot
            Map<Integer, List<Integer>> graph = new HashMap<>();
            Set<Integer> people = new HashSet<>();
            
            while (i < m && meetings[i][2] == time) {
                int x = meetings[i][0];
                int y = meetings[i][1];
                
                graph.computeIfAbsent(x, k -> new ArrayList<>()).add(y);
                graph.computeIfAbsent(y, k -> new ArrayList<>()).add(x);
                
                people.add(x);
                people.add(y);
                i++;
            }
            
            // For each person in this time slot, find connected components
            Set<Integer> visited = new HashSet<>();
            
            for (int person : people) {
                if (visited.contains(person)) {
                    continue;
                }
                
                // Find all people in this connected component
                List<Integer> component = new ArrayList<>();
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(person);
                visited.add(person);
                
                boolean hasSecret = false;
                
                while (!queue.isEmpty()) {
                    int curr = queue.poll();
                    component.add(curr);
                    
                    if (knowsSecret[curr]) {
                        hasSecret = true;
                    }
                    
                    // Add neighbors
                    if (graph.containsKey(curr)) {
                        for (int neighbor : graph.get(curr)) {
                            if (!visited.contains(neighbor)) {
                                visited.add(neighbor);
                                queue.offer(neighbor);
                            }
                        }
                    }
                }
                
                // If anyone in component knows secret, all learn it
                if (hasSecret) {
                    for (int p : component) {
                        knowsSecret[p] = true;
                    }
                }
            }
        }
        
        // Collect result
        List<Integer> result = new ArrayList<>();
        for (int j = 0; j < n; j++) {
            if (knowsSecret[j]) {
                result.add(j);
            }
        }
        return result;
    }
}