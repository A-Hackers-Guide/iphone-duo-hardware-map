# `WiFi3BarsNetwork`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `WiFiCandidateNetwork`
- 12 instance variables, 20 properties, 23 instance methods, 1 class methods

## Instance variables

```
B matched;
B _unwantedNetworkName;
I _venueType;
@"NSString" password;
@"NSSet" _attributes;
@"<TBScore>" _qualityScore;
@"<TBScore>" _popularityScore;
Q _type;
Q _venueGroup;
@"NSString" _uniqueIdentifier;
@"NSString" _SSID;
@"NSSet" _accessPoints;
```

## Properties

```
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",C,N,V_SSID) SSID;
@property (T@"NSSet",&,N,V_accessPoints) accessPoints;
@property (TB,N,V_unwantedNetworkName) unwantedNetworkName;
@property (T@"NSString",R,C,N,Vpassword) password;
@property (Tq,R,N) source;
@property (T@"NSSet",R,N,V_attributes) attributes;
@property (TB,N,Vmatched) matched;
@property (TQ,R,N,V_type) type;
@property (TQ,R,N,V_venueGroup) venueGroup;
@property (TI,R,N,V_venueType) venueType;
@property (T@"NSString",?,R,C,N) receivedFromDeviceName;
@property (T@"NSString",?,R,C,N) captiveToken;
@property (T@"NSString",?,R,C,N) captiveTokenAuthURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TBScore>",R,N,V_popularityScore) popularityScore;
@property (T@"<TBScore>",R,N,V_qualityScore) qualityScore;
```

## Class methods

```
+[WiFi3BarsNetwork supportsSecureCoding];
```

## Instance methods

```
-[WiFi3BarsNetwork accessPoints];
-[WiFi3BarsNetwork setSSID:];
-[WiFi3BarsNetwork venueGroup];
-[WiFi3BarsNetwork SSID];
-[WiFi3BarsNetwork setAccessPoints:];
-[WiFi3BarsNetwork unwantedNetworkName];
-[WiFi3BarsNetwork containsAccessPointMatchingBSSIDs:];
-[WiFi3BarsNetwork setUniqueIdentifier:];
-[WiFi3BarsNetwork setMatched:];
-[WiFi3BarsNetwork venueType];
-[WiFi3BarsNetwork uniqueIdentifier];
-[WiFi3BarsNetwork type];
-[WiFi3BarsNetwork initWithNetwork:];
-[WiFi3BarsNetwork encodeWithCoder:];
-[WiFi3BarsNetwork description];
-[WiFi3BarsNetwork initWithCoder:];
-[WiFi3BarsNetwork attributes];
-[WiFi3BarsNetwork setUnwantedNetworkName:];
-[WiFi3BarsNetwork qualityScore];
-[WiFi3BarsNetwork password];
-[WiFi3BarsNetwork source];
-[WiFi3BarsNetwork matched];
-[WiFi3BarsNetwork popularityScore];
```
