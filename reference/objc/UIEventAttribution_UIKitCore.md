# `UIEventAttribution`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
C _sourceIdentifier;
@"NSURL" _destinationURL;
@"NSURL" _reportEndpoint;
@"NSString" _sourceDescription;
@"NSString" _purchaser;
```

## Properties

```
@property (TC,R,N,V_sourceIdentifier) sourceIdentifier;
@property (T@"NSURL",R,C,N,V_destinationURL) destinationURL;
@property (T@"NSURL",R,C,N,V_reportEndpoint) reportEndpoint;
@property (T@"NSString",R,C,N,V_sourceDescription) sourceDescription;
@property (T@"NSString",R,C,N,V_purchaser) purchaser;
```

## Instance methods

```
-[UIEventAttribution toUISClickAttribution];
-[UIEventAttribution destinationURL];
-[UIEventAttribution purchaser];
-[UIEventAttribution initWithSourceIdentifier:destinationURL:sourceDescription:purchaser:];
-[UIEventAttribution sourceIdentifier];
-[UIEventAttribution reportEndpoint];
-[UIEventAttribution hash];
-[UIEventAttribution initWithSourceIdentifier:destinationURL:reportEndpoint:sourceDescription:purchaser:];
-[UIEventAttribution sourceDescription];
-[UIEventAttribution initWithUISClickAttribution:];
-[UIEventAttribution copyWithZone:];
-[UIEventAttribution isEqual:];
```
