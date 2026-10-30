# `MTLToolsResourceViewPool`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLResourceViewPoolGGDSPI`
- 0 instance variables, 8 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T{MTLResourceID=Q},R,N) baseResourceID;
@property (TQ,R,N) resourceViewCount;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R,N) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsResourceViewPool dealloc];
-[MTLToolsResourceViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:];
-[MTLToolsResourceViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:];
-[MTLToolsResourceViewPool initWithBaseObject:parent:];
```
