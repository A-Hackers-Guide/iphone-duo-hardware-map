# `MTLDynamicLibrary` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) installName;
```

## Instance methods

```
-[MTLDynamicLibrary device];
-[MTLDynamicLibrary label];
-[MTLDynamicLibrary setLabel:];
-[MTLDynamicLibrary installName];
-[MTLDynamicLibrary serializeToURL:error:];
```
