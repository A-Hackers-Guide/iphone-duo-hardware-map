# `UISClickAttribution`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
C _sourceIdentifier;
@"NSURL" _destinationURL;
@"NSURL" _reportEndpoint;
@"NSString" _sourceDescription;
@"NSString" _purchaser;
@"BKSHIDEventAuthenticationMessage" _eventMessage;
```

## Properties

```
@property (TC,R,N,V_sourceIdentifier) sourceIdentifier;
@property (T@"NSURL",R,C,N,V_destinationURL) destinationURL;
@property (T@"NSURL",R,C,N,V_reportEndpoint) reportEndpoint;
@property (T@"NSString",R,C,N,V_sourceDescription) sourceDescription;
@property (T@"NSString",R,C,N,V_purchaser) purchaser;
@property (T@"BKSHIDEventAuthenticationMessage",R,C,N,V_eventMessage) eventMessage;
```

## Class methods

```
+[UISClickAttribution supportsSecureCoding];
```

## Instance methods

```
-[UISClickAttribution destinationURL];
-[UISClickAttribution purchaser];
-[UISClickAttribution sourceIdentifier];
-[UISClickAttribution reportEndpoint];
-[UISClickAttribution encodeWithCoder:];
-[UISClickAttribution hash];
-[UISClickAttribution initWithCoder:];
-[UISClickAttribution sourceDescription];
-[UISClickAttribution copyWithZone:];
-[UISClickAttribution isEqual:];
-[UISClickAttribution initWithSourceIdentifier:destinationURL:reportEndpoint:sourceDescription:purchaser:eventMessage:];
-[UISClickAttribution clickAttributionWithReportEndpoint:];
-[UISClickAttribution eventMessage];
```
