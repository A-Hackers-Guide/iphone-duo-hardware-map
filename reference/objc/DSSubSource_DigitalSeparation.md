# `DSSubSource`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSSource`
- 2 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<DSSource>" _parentSource;
@"NSString" _resourceName;
```

## Properties

```
@property (T@"<DSSource>",&,N,V_parentSource) parentSource;
@property (T@"NSString",C,N,V_resourceName) resourceName;
@property (T@"NSString",R,C,N) name;
@property (T@"NSArray",?,R,C,N) resourceNames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSSubSource name];
-[DSSubSource resourceName];
-[DSSubSource setResourceName:];
-[DSSubSource stopAllSharingWithCompletion:];
-[DSSubSource fetchSharedResourcesWithCompletion:];
-[DSSubSource stopSharing:withCompletion:];
-[DSSubSource stopSharingWithParticipant:completion:];
-[DSSubSource parentSource];
-[DSSubSource setParentSource:];
-[DSSubSource init:withResourceName:];
```
