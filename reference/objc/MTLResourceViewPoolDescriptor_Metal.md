# `MTLResourceViewPoolDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _label;
Q _resourceViewCount;
B _forceBaseResourceID;
Q _baseResourceID;
```

## Properties

```
@property (TB,N) forceBaseResourceID;
@property (TQ,N) baseResourceID;
@property (TQ,N,V_resourceViewCount) resourceViewCount;
@property (T@"NSString",C,N,V_label) label;
```

## Instance methods

```
-[MTLResourceViewPoolDescriptor init];
-[MTLResourceViewPoolDescriptor label];
-[MTLResourceViewPoolDescriptor setLabel:];
-[MTLResourceViewPoolDescriptor dealloc];
-[MTLResourceViewPoolDescriptor hash];
-[MTLResourceViewPoolDescriptor copyWithZone:];
-[MTLResourceViewPoolDescriptor isEqual:];
-[MTLResourceViewPoolDescriptor baseResourceID];
-[MTLResourceViewPoolDescriptor forceBaseResourceID];
-[MTLResourceViewPoolDescriptor resourceViewCount];
-[MTLResourceViewPoolDescriptor setBaseResourceID:];
-[MTLResourceViewPoolDescriptor setForceBaseResourceID:];
-[MTLResourceViewPoolDescriptor setResourceViewCount:];
```
