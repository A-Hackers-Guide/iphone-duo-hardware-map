# `TBLocationFetchRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchRequest`, `NSCopying`
- 6 instance variables, 10 properties, 16 instance methods, 2 class methods

## Instance variables

```
B _cacheable;
Q _sourcePolicy;
@"NSDictionary" userInfo;
@? resultsHandler;
@? preferLocalHandler;
@"TBLocationFetchRequestDescriptor" _descriptor;
```

## Properties

```
@property (T@"TBLocationFetchRequestDescriptor",&,N,V_descriptor) descriptor;
@property (TB,N,V_cacheable) cacheable;
@property (TQ,N,V_sourcePolicy) sourcePolicy;
@property (T@?,C,N,VresultsHandler) resultsHandler;
@property (T@?,C,N,VpreferLocalHandler) preferLocalHandler;
@property (T@"NSDictionary",?,&,N,VuserInfo) userInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBLocationFetchRequest fetchRequestWithDescriptor:sourcePolicy:];
+[TBLocationFetchRequest fetchRequestWithDescriptor:sourcePolicy:cacheable:];
```

## Instance methods

```
-[TBLocationFetchRequest cacheable];
-[TBLocationFetchRequest setDescriptor:];
-[TBLocationFetchRequest initWithDescriptor:sourcePolicy:cacheable:];
-[TBLocationFetchRequest descriptor];
-[TBLocationFetchRequest userInfo];
-[TBLocationFetchRequest setResultsHandler:];
-[TBLocationFetchRequest setUserInfo:];
-[TBLocationFetchRequest setCacheable:];
-[TBLocationFetchRequest sourcePolicy];
-[TBLocationFetchRequest handleResponse:];
-[TBLocationFetchRequest handlePreferLocalResponse:];
-[TBLocationFetchRequest resultsHandler];
-[TBLocationFetchRequest setPreferLocalHandler:];
-[TBLocationFetchRequest preferLocalHandler];
-[TBLocationFetchRequest copyWithZone:];
-[TBLocationFetchRequest setSourcePolicy:];
```
