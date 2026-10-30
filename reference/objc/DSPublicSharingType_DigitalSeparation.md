# `DSPublicSharingType`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"<DSSource>" _source;
@"NSMutableSet" _publicResources;
```

## Properties

```
@property (T@"<DSSource>",&,N,V_source) source;
@property (T@"NSMutableSet",&,N,V_publicResources) publicResources;
@property (Tq,R,N) score;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) localizedDetailText;
@property (T@"NSArray",R,C,N) allPublicResources;
```

## Class methods

```
+[DSPublicSharingType initialize];
```

## Instance methods

```
-[DSPublicSharingType initWithSource:];
-[DSPublicSharingType displayName];
-[DSPublicSharingType score];
-[DSPublicSharingType setSource:];
-[DSPublicSharingType hash];
-[DSPublicSharingType isEqual:];
-[DSPublicSharingType source];
-[DSPublicSharingType localizedDetailText];
-[DSPublicSharingType publicResources];
-[DSPublicSharingType addPublicResource:];
-[DSPublicSharingType allPublicResources];
-[DSPublicSharingType removePublicResource:];
-[DSPublicSharingType setPublicResources:];
-[DSPublicSharingType stopAllSharingOnQueue:completion:];
-[DSPublicSharingType stopSharingResource:onQueue:completion:];
```
