xquery version "3.1" encoding "UTF-8";

let $msg := 'Hello XQuery'
return
  <results timestamp="{current-dateTime()}">
     <message>{$msg}</message>
  </results>
