# `WiFiCandidateNetwork` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `TBScorable`
- 0 instance variables, 13 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) SSID;
@property (T@"NSSet",R,N) accessPoints;
@property (T@"NSString",R,C,N) password;
@property (Tq,R,N) source;
@property (T@"NSSet",R,N) attributes;
@property (TB,N) matched;
@property (TQ,R,N) type;
@property (TQ,R,N) venueGroup;
@property (TI,R,N) venueType;
@property (T@"NSString",?,R,C,N) uniqueIdentifier;
@property (T@"NSString",?,R,C,N) receivedFromDeviceName;
@property (T@"NSString",?,R,C,N) captiveToken;
@property (T@"NSString",?,R,C,N) captiveTokenAuthURL;
```

## Instance methods

```
-[WiFiCandidateNetwork accessPoints];
-[WiFiCandidateNetwork setSSID:];
-[WiFiCandidateNetwork venueGroup];
-[WiFiCandidateNetwork SSID];
-[WiFiCandidateNetwork containsAccessPointMatchingBSSIDs:];
-[WiFiCandidateNetwork setMatched:];
-[WiFiCandidateNetwork venueType];
-[WiFiCandidateNetwork type];
-[WiFiCandidateNetwork attributes];
-[WiFiCandidateNetwork password];
-[WiFiCandidateNetwork source];
-[WiFiCandidateNetwork matched];
-[WiFiCandidateNetwork uniqueIdentifier];
-[WiFiCandidateNetwork captiveToken];
-[WiFiCandidateNetwork captiveTokenAuthURL];
-[WiFiCandidateNetwork receivedFromDeviceName];
```
