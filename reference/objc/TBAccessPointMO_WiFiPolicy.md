# `TBAccessPointMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- Protocols: `TBAccessPoint`, `NSSecureCoding`, `NSCoding`
- 0 instance variables, 20 properties, 10 instance methods, 5 class methods

## Properties

```
@property (T@"NSString",R,N) BSSID;
@property (Td,R,N) latitude;
@property (Td,R,N) longitude;
@property (TB,R,N,GisEdge) edge;
@property (TB,R,N,GisTCPGood) TCPGood;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TBScore>",R,N) popularityScore;
@property (T@"<TBScore>",R,N) qualityScore;
@property (T@"NSString",C,D,N) bssid;
@property (T@"NSDate",C,D,N) created;
@property (TB,D,N) edge;
@property (Td,D,N) lat;
@property (Td,D,N) lng;
@property (Ti,D,N) popularityScoreValue;
@property (Ti,D,N) qualityScoreValue;
@property (TB,D,N) tcpGood;
@property (T@"TBNetworkMO",&,D,N) network;
```

## Class methods

```
+[TBAccessPointMO supportsSecureCoding];
+[TBAccessPointMO fetchRequest];
+[TBAccessPointMO entityName];
+[TBAccessPointMO generateNewAccessPointObjectFromMOC:];
+[TBAccessPointMO removeAllAccessPointsInMOC:];
```

## Instance methods

```
-[TBAccessPointMO BSSID];
-[TBAccessPointMO latitude];
-[TBAccessPointMO longitude];
-[TBAccessPointMO encodeWithCoder:];
-[TBAccessPointMO initWithCoder:];
-[TBAccessPointMO qualityScore];
-[TBAccessPointMO popularityScore];
-[TBAccessPointMO dictionaryRepresentation];
-[TBAccessPointMO isEdge];
-[TBAccessPointMO isTCPGood];
```
