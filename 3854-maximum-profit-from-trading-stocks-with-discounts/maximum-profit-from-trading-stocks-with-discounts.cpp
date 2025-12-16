class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> adj(n + 1);
        for (auto& h : hierarchy) {
            adj[h[0]].push_back(h[1]);
        }
        
        // memo[u][b][d] = max profit for subtree rooted at u with budget b
        // d = 0: parent didn't buy, 1: parent bought
        vector<vector<vector<int>>> memo(n + 1, 
            vector<vector<int>>(budget + 1, vector<int>(2, -1)));
        
        function<void(int)> dfs = [&](int u) {
            // Process children first (post-order traversal)
            for (int v : adj[u]) {
                dfs(v);
            }
            
            // Now compute dp for this node
            for (int parentBought = 0; parentBought <= 1; parentBought++) {
                // Current node's costs and profits
                int cost_full = present[u - 1];
                int cost_half = cost_full / 2;
                int profit_full = future[u - 1] - cost_full;
                int profit_half = future[u - 1] - cost_half;
                
                // Initialize dp arrays for this node
                vector<int> dp_no_buy(budget + 1, -1e9);
                vector<int> dp_buy(budget + 1, -1e9);
                
                // Base: don't buy current node
                dp_no_buy[0] = 0;
                
                // Base: buy current node
                int buy_cost = parentBought ? cost_half : cost_full;
                int buy_profit = parentBought ? profit_half : profit_full;
                if (buy_cost <= budget) {
                    dp_buy[buy_cost] = buy_profit;
                }
                
                // Merge children
                for (int v : adj[u]) {
                    vector<int> new_dp_no_buy(budget + 1, -1e9);
                    vector<int> new_dp_buy(budget + 1, -1e9);
                    
                    // Merge dp_no_buy with child's no-discount case
                    for (int i = 0; i <= budget; i++) {
                        if (dp_no_buy[i] <= -1e8) continue;
                        for (int j = 0; i + j <= budget; j++) {
                            // Child doesn't get discount
                            if (memo[v][j][0] > -1e8) {
                                new_dp_no_buy[i + j] = max(new_dp_no_buy[i + j], 
                                    dp_no_buy[i] + memo[v][j][0]);
                            }
                        }
                    }
                    
                    // Merge dp_buy with child's discount case
                    for (int i = 0; i <= budget; i++) {
                        if (dp_buy[i] <= -1e8) continue;
                        for (int j = 0; i + j <= budget; j++) {
                            // Child gets discount (since we bought)
                            if (memo[v][j][1] > -1e8) {
                                new_dp_buy[i + j] = max(new_dp_buy[i + j], 
                                    dp_buy[i] + memo[v][j][1]);
                            }
                        }
                    }
                    
                    dp_no_buy = new_dp_no_buy;
                    dp_buy = new_dp_buy;
                }
                
                // Store results in memo
                for (int b = 0; b <= budget; b++) {
                    memo[u][b][parentBought] = max(dp_no_buy[b], dp_buy[b]);
                    if (memo[u][b][parentBought] < 0) memo[u][b][parentBought] = -1e9;
                }
            }
        };
        
        dfs(1);
        
        int ans = 0;
        for (int b = 0; b <= budget; b++) {
            ans = max(ans, memo[1][b][0]);  // Root has no parent
        }
        return ans;
    }
};