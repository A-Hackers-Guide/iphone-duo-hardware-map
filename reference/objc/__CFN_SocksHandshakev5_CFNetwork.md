# `__CFN_SocksHandshakev5`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__CFN_SocksHandshake`
- 14 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
B _done;
Q _state;
i _numberOfAuthVersionSupported;
@"NSMutableSet" _authMethods;
C _addressType;
i _destinationLen;
@"NSMutableString" _domainName;
[16C] ipaddr;
i _portLen;
S _destPort;
i _usernameLen;
@"NSMutableString" _username;
i _passwordLen;
@"NSMutableString" _password;
```

## Instance methods

```
-[__CFN_SocksHandshakev5 finish:];
-[__CFN_SocksHandshakev5 parse:len:completion:];
```
