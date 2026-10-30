# `UINibStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" bundleResourceName;
@"NSString" bundleDirectoryName;
@"NSBundle" bundle;
@"NSString" identifierForStringsFile;
@"NSData" archiveData;
@"UINibDecoder" nibDecoder;
B instantiatingForSimulator;
B captureImplicitLoadingContextOnDecode;
```

## Properties

```
@property (T@"NSString",C,N,VbundleResourceName) bundleResourceName;
@property (T@"NSString",C,N,VbundleDirectoryName) bundleDirectoryName;
@property (T@"NSBundle",&,N,Vbundle) bundle;
@property (T@"NSString",C,N,VidentifierForStringsFile) identifierForStringsFile;
@property (T@"NSData",C,N,VarchiveData) archiveData;
@property (T@"UINibDecoder",&,N,VnibDecoder) nibDecoder;
@property (TB,N,VinstantiatingForSimulator) instantiatingForSimulator;
@property (TB,VcaptureImplicitLoadingContextOnDecode) captureImplicitLoadingContextOnDecode;
```

## Instance methods

```
-[UINibStorage bundle];
-[UINibStorage setBundleDirectoryName:];
-[UINibStorage setIdentifierForStringsFile:];
-[UINibStorage instantiatingForSimulator];
-[UINibStorage bundleDirectoryName];
-[UINibStorage nibDecoder];
-[UINibStorage identifierForStringsFile];
-[UINibStorage setBundle:];
-[UINibStorage bundleResourceName];
-[UINibStorage captureImplicitLoadingContextOnDecode];
-[UINibStorage archiveData];
-[UINibStorage setBundleResourceName:];
-[UINibStorage setArchiveData:];
-[UINibStorage setInstantiatingForSimulator:];
-[UINibStorage setNibDecoder:];
-[UINibStorage setCaptureImplicitLoadingContextOnDecode:];
```
