select case 
            when P is Null then concat(N, " Root")
            when N not in (select distinct(P) from BST where P is not NUll) then concat(N, " Leaf")
            Else concat(N, " Inner")
            End as "Name"
            from BST
            Order by N asc
            
            
            
            
            
            
