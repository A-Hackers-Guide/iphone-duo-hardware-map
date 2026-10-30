# `_MTLFunctionHandle`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLFunctionHandleSPI`
- 3 instance variables, 9 properties, 7 instance methods, 0 class methods

## Instance variables

```
Q _functionType;
@"NSString" _name;
@"<MTLDevice>" _device;
```

## Properties

```
@property (TQ,R) functionType;
@property (T@"NSString",R) name;
@property (T@"<MTLDevice>",R) device;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) resourceIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLFunctionHandle resourceIndex];
-[_MTLFunctionHandle functionType];
-[_MTLFunctionHandle device];
-[_MTLFunctionHandle dealloc];
-[_MTLFunctionHandle gpuResourceID];
-[_MTLFunctionHandle name];
-[_MTLFunctionHandle initWithFunctionType:name:device:];
```
