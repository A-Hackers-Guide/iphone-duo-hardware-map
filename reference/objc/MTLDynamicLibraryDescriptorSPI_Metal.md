# `MTLDynamicLibraryDescriptorSPI`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _url;
@"<MTLLibrary>" _library;
Q _options;
Q _globalConstantsTag;
```

## Properties

```
@property (T@"<MTLLibrary>",&,N,V_library) library;
@property (T@"NSURL",C,N,V_url) url;
@property (TQ,N,V_options) options;
@property (TQ,N,V_globalConstantsTag) globalConstantsTag;
```

## Instance methods

```
-[MTLDynamicLibraryDescriptorSPI setLibrary:];
-[MTLDynamicLibraryDescriptorSPI setOptions:];
-[MTLDynamicLibraryDescriptorSPI dealloc];
-[MTLDynamicLibraryDescriptorSPI setGlobalConstantsTag:];
-[MTLDynamicLibraryDescriptorSPI hash];
-[MTLDynamicLibraryDescriptorSPI library];
-[MTLDynamicLibraryDescriptorSPI options];
-[MTLDynamicLibraryDescriptorSPI globalConstantsTag];
-[MTLDynamicLibraryDescriptorSPI setUrl:];
-[MTLDynamicLibraryDescriptorSPI copyWithZone:];
-[MTLDynamicLibraryDescriptorSPI isEqual:];
-[MTLDynamicLibraryDescriptorSPI url];
```
