# 目次
- [apexRPCalculator.py](#apexRPCalculator.py)
- [frequency.py なろう小説の更新頻度](#frequency.py)

# apexRPCalculator.py
必要なRPとコストを入力することで何位で何キル/アシストすればいいか表示するやつ  
get how many kill/assist and rank by enter the need rp and the cost
  
## usage
```python apexRPCalculator.py [need] [cost]```  
or  
```{#lst:id python caption="apex"}
import apexRPCalculator  
apexRPCalculator.getLeast([need], [cost]) # => return list [[place, kill/assist, rp] , ...]
```  

# frequency.py
なろう小説のurlを入力すると更新頻度をグラフ化するやつ  
