# onlinepaste
Internet clipboard

This started as a hobby project while learning Django. It was meant to improve or add several features I found lacking in the "Internet Clipboards" I use. 

The following are some of the useful features:
  1) Password protection - Many sites require paid subscription for this. This uses In-browser encryption for password protected texts.
  2) In-browser encryption - Uses the https://crypto.stanford.edu/sjcl/ to encrypt password protected texts. Plaintext pertaining to password protected clips is never sent unencrypted over the internet and is also not stored uncrypted on the server. 
  3) Custom keyword option.
  4) Multiple Clip Expiry options.

You can checkout the code in action at http://onlinepaste.net
