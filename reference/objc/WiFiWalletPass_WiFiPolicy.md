# `WiFiWalletPass`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiCandidateNetwork`
- 17 instance variables, 23 properties, 30 instance methods, 0 class methods

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
@"NSString" _uniqueIdentifier;
@"NSString" _passTypeIdentifier;
@"NSString" _serialNumber;
@"NSDate" _relevantDate;
@"NSString" _localizedDescription;
@"NSString" _captiveToken;
@"NSString" _captiveTokenAuthURL;
```

## Properties

```
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",C,N,V_passTypeIdentifier) passTypeIdentifier;
@property (T@"NSString",C,N,V_serialNumber) serialNumber;
@property (T@"NSDate",C,N,V_relevantDate) relevantDate;
@property (T@"NSString",C,N,V_localizedDescription) localizedDescription;
@property (T@"NSString",C,N,VSSID) SSID;
@property (T@"NSString",C,N,Vpassword) password;
@property (T@"NSString",C,N,V_captiveToken) captiveToken;
@property (T@"NSString",C,N,V_captiveTokenAuthURL) captiveTokenAuthURL;
@property (T@"NSSet",R,N,VaccessPoints) accessPoints;
@property (Tq,R,N) source;
@property (T@"NSSet",R,N,Vattributes) attributes;
@property (TB,N,Vmatched) matched;
@property (TQ,R,N,Vtype) type;
@property (TQ,R,N,VvenueGroup) venueGroup;
@property (TI,R,N,VvenueType) venueType;
@property (T@"NSString",?,R,C,N) receivedFromDeviceName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TBScore>",R,N,VpopularityScore) popularityScore;
@property (T@"<TBScore>",R,N,VqualityScore) qualityScore;
```

## Instance methods

```
-[WiFiWalletPass accessPoints];
-[WiFiWalletPass setSerialNumber:];
-[WiFiWalletPass setSSID:];
-[WiFiWalletPass venueGroup];
-[WiFiWalletPass localizedDescription];
-[WiFiWalletPass SSID];
-[WiFiWalletPass containsAccessPointMatchingBSSIDs:];
-[WiFiWalletPass setUniqueIdentifier:];
-[WiFiWalletPass serialNumber];
-[WiFiWalletPass setMatched:];
-[WiFiWalletPass venueType];
-[WiFiWalletPass uniqueIdentifier];
-[WiFiWalletPass type];
-[WiFiWalletPass description];
-[WiFiWalletPass setLocalizedDescription:];
-[WiFiWalletPass attributes];
-[WiFiWalletPass setPassword:];
-[WiFiWalletPass qualityScore];
-[WiFiWalletPass password];
-[WiFiWalletPass source];
-[WiFiWalletPass matched];
-[WiFiWalletPass popularityScore];
-[WiFiWalletPass passTypeIdentifier];
-[WiFiWalletPass setPassTypeIdentifier:];
-[WiFiWalletPass relevantDate];
-[WiFiWalletPass setRelevantDate:];
-[WiFiWalletPass captiveToken];
-[WiFiWalletPass captiveTokenAuthURL];
-[WiFiWalletPass setCaptiveToken:];
-[WiFiWalletPass setCaptiveTokenAuthURL:];
```
