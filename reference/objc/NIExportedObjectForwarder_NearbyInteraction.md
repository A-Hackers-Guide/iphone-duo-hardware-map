# `NIExportedObjectForwarder`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@ _exportedObject;
# _exportedObjectClass;
```

## Properties

```
@property (T@,W,N,V_exportedObject) exportedObject;
@property (T#,&,N,V_exportedObjectClass) exportedObjectClass;
```

## Instance methods

```
-[NIExportedObjectForwarder forwardingTargetForSelector:];
-[NIExportedObjectForwarder exportedObject];
-[NIExportedObjectForwarder setExportedObject:];
-[NIExportedObjectForwarder methodSignatureForSelector:];
-[NIExportedObjectForwarder forwardInvocation:];
-[NIExportedObjectForwarder exportedObjectClass];
-[NIExportedObjectForwarder initWithExportedObject:];
-[NIExportedObjectForwarder setExportedObjectClass:];
```
