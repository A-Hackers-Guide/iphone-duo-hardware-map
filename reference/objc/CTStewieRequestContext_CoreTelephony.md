# `CTStewieRequestContext`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
q _reason;
@"NSDictionary" _metadata;
@"NSData" _epki;
@"NSData" _shared;
```

## Properties

```
@property (Tq,N,V_reason) reason;
@property (T@"NSDictionary",&,N,V_metadata) metadata;
@property (T@"NSData",&,N,V_epki) epki;
@property (T@"NSData",&,N,V_shared) shared;
```

## Class methods

```
+[CTStewieRequestContext supportsSecureCoding];
```

## Instance methods

```
-[CTStewieRequestContext setShared:];
-[CTStewieRequestContext setReason:];
-[CTStewieRequestContext metadata];
-[CTStewieRequestContext encodeWithCoder:];
-[CTStewieRequestContext setMetadata:];
-[CTStewieRequestContext description];
-[CTStewieRequestContext initWithCoder:];
-[CTStewieRequestContext shared];
-[CTStewieRequestContext reason];
-[CTStewieRequestContext copyWithZone:];
-[CTStewieRequestContext isEqual:];
-[CTStewieRequestContext epki];
-[CTStewieRequestContext isEqualToRequestContext:];
-[CTStewieRequestContext setEpki:];
```
