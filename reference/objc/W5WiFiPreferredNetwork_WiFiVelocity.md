# `W5WiFiPreferredNetwork`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 11 instance variables, 11 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _isEnabled;
B _isPasspoint;
B _isCaptive;
B _isHidden;
B _isMultiAP;
@"NSString" _identifier;
@"NSString" _ssidString;
@"NSData" _ssid;
q _security;
@"NSString" _domainName;
@"NSDate" _lastJoinedTimestamp;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_ssidString) ssidString;
@property (T@"NSData",C,N,V_ssid) ssid;
@property (Tq,N,V_security) security;
@property (TB,N,V_isEnabled) isEnabled;
@property (TB,N,V_isPasspoint) isPasspoint;
@property (T@"NSString",C,N,V_domainName) domainName;
@property (TB,N,V_isCaptive) isCaptive;
@property (TB,N,V_isHidden) isHidden;
@property (TB,N,V_isMultiAP) isMultiAP;
@property (T@"NSDate",C,N,V_lastJoinedTimestamp) lastJoinedTimestamp;
```

## Class methods

```
+[W5WiFiPreferredNetwork supportsSecureCoding];
```

## Instance methods

```
-[W5WiFiPreferredNetwork domainName];
-[W5WiFiPreferredNetwork setIsHidden:];
-[W5WiFiPreferredNetwork ssid];
-[W5WiFiPreferredNetwork setSsid:];
-[W5WiFiPreferredNetwork identifier];
-[W5WiFiPreferredNetwork setIsEnabled:];
-[W5WiFiPreferredNetwork dealloc];
-[W5WiFiPreferredNetwork setIsPasspoint:];
-[W5WiFiPreferredNetwork setIsCaptive:];
-[W5WiFiPreferredNetwork isEnabled];
-[W5WiFiPreferredNetwork setIdentifier:];
-[W5WiFiPreferredNetwork isHidden];
-[W5WiFiPreferredNetwork isPasspoint];
-[W5WiFiPreferredNetwork encodeWithCoder:];
-[W5WiFiPreferredNetwork isCaptive];
-[W5WiFiPreferredNetwork conformsToProtocol:];
-[W5WiFiPreferredNetwork hash];
-[W5WiFiPreferredNetwork security];
-[W5WiFiPreferredNetwork description];
-[W5WiFiPreferredNetwork initWithCoder:];
-[W5WiFiPreferredNetwork copyWithZone:];
-[W5WiFiPreferredNetwork isEqual:];
-[W5WiFiPreferredNetwork setSecurity:];
-[W5WiFiPreferredNetwork setDomainName:];
-[W5WiFiPreferredNetwork ssidString];
-[W5WiFiPreferredNetwork isEqualToPreferredNetwork:];
-[W5WiFiPreferredNetwork isMultiAP];
-[W5WiFiPreferredNetwork lastJoinedTimestamp];
-[W5WiFiPreferredNetwork setIsMultiAP:];
-[W5WiFiPreferredNetwork setLastJoinedTimestamp:];
-[W5WiFiPreferredNetwork setSsidString:];
```
