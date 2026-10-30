# `WiFiAvailabilityNearbyCandidateNetwork`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiCandidateNetwork`
- 11 instance variables, 19 properties, 16 instance methods, 0 class methods

## Instance variables

```
B matched;
I venueType;
@"NSString" SSID;
@"NSString" password;
@"NSSet" attributes;
@"NSSet" accessPoints;
@"<TBScore>" qualityScore;
@"<TBScore>" popularityScore;
Q venueGroup;
Q type;
@"NSString" receivedFromDeviceName;
```

## Properties

```
@property (T@"NSString",C,N,VreceivedFromDeviceName) receivedFromDeviceName;
@property (T@"NSString",C,N,VSSID) SSID;
@property (T@"NSSet",R,N,VaccessPoints) accessPoints;
@property (T@"NSString",R,C,N,Vpassword) password;
@property (Tq,R,N) source;
@property (T@"NSSet",R,N,Vattributes) attributes;
@property (TB,N,Vmatched) matched;
@property (TQ,R,N,Vtype) type;
@property (TQ,R,N,VvenueGroup) venueGroup;
@property (TI,R,N,VvenueType) venueType;
@property (T@"NSString",?,R,C,N) uniqueIdentifier;
@property (T@"NSString",?,R,C,N) captiveToken;
@property (T@"NSString",?,R,C,N) captiveTokenAuthURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TBScore>",R,N,VpopularityScore) popularityScore;
@property (T@"<TBScore>",R,N,VqualityScore) qualityScore;
```

## Instance methods

```
-[WiFiAvailabilityNearbyCandidateNetwork accessPoints];
-[WiFiAvailabilityNearbyCandidateNetwork setSSID:];
-[WiFiAvailabilityNearbyCandidateNetwork venueGroup];
-[WiFiAvailabilityNearbyCandidateNetwork SSID];
-[WiFiAvailabilityNearbyCandidateNetwork containsAccessPointMatchingBSSIDs:];
-[WiFiAvailabilityNearbyCandidateNetwork setMatched:];
-[WiFiAvailabilityNearbyCandidateNetwork venueType];
-[WiFiAvailabilityNearbyCandidateNetwork type];
-[WiFiAvailabilityNearbyCandidateNetwork attributes];
-[WiFiAvailabilityNearbyCandidateNetwork qualityScore];
-[WiFiAvailabilityNearbyCandidateNetwork password];
-[WiFiAvailabilityNearbyCandidateNetwork source];
-[WiFiAvailabilityNearbyCandidateNetwork matched];
-[WiFiAvailabilityNearbyCandidateNetwork popularityScore];
-[WiFiAvailabilityNearbyCandidateNetwork receivedFromDeviceName];
-[WiFiAvailabilityNearbyCandidateNetwork setReceivedFromDeviceName:];
```
