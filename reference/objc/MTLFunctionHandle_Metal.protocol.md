# `MTLFunctionHandle` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TQ,R) functionType;
@property (T@"NSString",R) name;
@property (T@"<MTLDevice>",R) device;
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Instance methods

```
-[MTLFunctionHandle functionType];
-[MTLFunctionHandle device];
-[MTLFunctionHandle gpuResourceID];
-[MTLFunctionHandle name];
```
