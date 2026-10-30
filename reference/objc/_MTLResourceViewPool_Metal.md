# `_MTLResourceViewPool`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLResourceViewPoolGGDSPI`
- 3 instance variables, 8 properties, 7 instance methods, 0 class methods

## Instance variables

```
{MTLResourceID="_impl"Q} _baseResourceID;
Q _resourceViewCount;
@"<MTLDevice>" _device;
```

## Properties

```
@property (T{MTLResourceID=Q},R,N) baseResourceID;
@property (TQ,R,N) resourceViewCount;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",R,N) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLResourceViewPool device];
-[_MTLResourceViewPool dealloc];
-[_MTLResourceViewPool baseResourceID];
-[_MTLResourceViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:];
-[_MTLResourceViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:];
-[_MTLResourceViewPool initWithDescriptor:device:];
-[_MTLResourceViewPool resourceViewCount];
```
