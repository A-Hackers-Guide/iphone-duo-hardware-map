# `AVMediaFileType`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 6 properties, 12 instance methods, 6 class methods

## Instance variables

```
@"NSString" _uti;
@"AVDispatchOnce" _supportsSampleReferencesOnce;
B _supportsSampleReferences;
```

## Properties

```
@property (T@"NSString",R,N) defaultFileExtension;
@property (T@"NSSet",R,N) supportedMediaTypes;
@property (TB,R,N) supportsSampleReferences;
@property (T@"NSString",R,N) UTI;
@property (T@"NSString",R,N) figFormatReaderFileFormat;
@property (TI,R,N) audioFileTypeID;
```

## Class methods

```
+[AVMediaFileType initialize];
+[AVMediaFileType _mediaFileTypeWithFileTypeIdentifier:exceptionReason:];
+[AVMediaFileType allFileTypeIdentifiers];
+[AVMediaFileType figFileTypeProfileFromAVFileTypeProfile:];
+[AVMediaFileType isoFileTypes];
+[AVMediaFileType mediaFileTypeWithFileTypeIdentifier:];
```

## Instance methods

```
-[AVMediaFileType UTI];
-[AVMediaFileType dealloc];
-[AVMediaFileType description];
-[AVMediaFileType supportedMediaTypes];
-[AVMediaFileType copyWithZone:];
-[AVMediaFileType audioFileTypeID];
-[AVMediaFileType supportsFormat:];
-[AVMediaFileType defaultFileExtension];
-[AVMediaFileType figFormatReaderFileFormat];
-[AVMediaFileType initWithFileTypeIdentifier:exceptionReason:];
-[AVMediaFileType supportsOutputSettings:reason:];
-[AVMediaFileType supportsSampleReferences];
```
