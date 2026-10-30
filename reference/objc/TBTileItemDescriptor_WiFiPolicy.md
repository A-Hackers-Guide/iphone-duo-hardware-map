# `TBTileItemDescriptor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBTileRequestItem`
- 2 instance variables, 6 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSString" _etag;
@"NSNumber" _key;
```

## Properties

```
@property (T@"NSNumber",&,N,V_key) key;
@property (T@"NSString",C,N,V_etag) etag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBTileItemDescriptor tileItemDescriptorWithKey:];
```

## Instance methods

```
-[TBTileItemDescriptor etag];
-[TBTileItemDescriptor setEtag:];
-[TBTileItemDescriptor setKey:];
-[TBTileItemDescriptor copyWithZone:];
-[TBTileItemDescriptor key];
-[TBTileItemDescriptor initWithKey:etag:];
```
