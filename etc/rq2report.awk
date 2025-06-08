BEGIN { FS=OFS="," }
      { print
        for(i=1;i<=NF;i++)  n[i] +=  $i ~ /A/ }          
END   { s=sep=""
        for(i=1;i<=NF;i++) {
          s1 = n[i] ? int(100*n[i]/NR) : " "
          s   = s sep s1 
          sep = ", "}
        print(s"A") }
