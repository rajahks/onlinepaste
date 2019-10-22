# onlinepaste
Internet clipboard

This started as a hobby project while learning Django. It is meant to improve or add several features I found lacking in the "Internet Clipboards" I use and also combine them into a single site. 

The following are some of the useful features:
  1) Password protection without storing passwords -  Many sites require paid subscription for this. Onlinepaste uses In-browser 
     encryption for password protected texts and never sends the password to the server.
  2) In-browser encryption - Uses the https://crypto.stanford.edu/sjcl/ to encrypt password protected texts. Plaintext pertaining 
     to password protected clips is never sent unencrypted over the internet and is also not stored un-encrypted on the server. 
  3) Custom keyword option.
  4) Multiple Clip Expiry options.
  5) Single click copy of the URL and clip text.

You can checkout the code in action at http://onlinepaste.net

Note: Work-in-progress and many more features,fixes in queue.
