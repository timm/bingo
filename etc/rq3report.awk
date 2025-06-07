BEGIN { FS=OFS="," }
      { print
        for(i=1;i<=NF;i++)  n[i] +=  $i ~ /A/ }          
END   { s=sep=""
        for(i=1;i<=NF;i++) {
          s   = s sep int(100*n[i]/NR)
          sep = ", "}
        print(s"A") }


