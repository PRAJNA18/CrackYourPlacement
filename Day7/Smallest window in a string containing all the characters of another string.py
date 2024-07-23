def min_win(s, t):
    if not t or not s:
        return ""
    
    cnt_t = {}
    for c in t:
        cnt_t[c] = cnt_t.get(c, 0) + 1
    
    req = len(cnt_t)
    
    l, r = 0, 0
    form = 0
    win_cnt = {}
    
    ans = float("inf"), None, None
    
    while r < len(s):
        c = s[r]
        win_cnt[c] = win_cnt.get(c, 0) + 1
        
        if c in cnt_t and win_cnt[c] == cnt_t[c]:
            form += 1
        
        while l <= r and form == req:
            c = s[l]
            
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            
            win_cnt[c] -= 1
            if c in cnt_t and win_cnt[c] < cnt_t[c]:
                form -= 1
            
            l += 1    
        
        r += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]