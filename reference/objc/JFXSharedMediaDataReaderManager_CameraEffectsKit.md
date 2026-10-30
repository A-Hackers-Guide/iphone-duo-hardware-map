# `JFXSharedMediaDataReaderManager`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<JFXPlayableElement>" _playableElement;
@"JFXARMetadataMediaReader" _weakSharedARMetadataReader;
@"JFXDepthDataMediaReader" _weakSharedDepthDataReader;
```

## Properties

```
@property (T@"<JFXPlayableElement>",&,N,V_playableElement) playableElement;
@property (T@"JFXARMetadataMediaReader",W,N,V_weakSharedARMetadataReader) weakSharedARMetadataReader;
@property (T@"JFXDepthDataMediaReader",W,N,V_weakSharedDepthDataReader) weakSharedDepthDataReader;
@property (T@"JFXARMetadataMediaReader",R,N) sharedARMetadataReader;
@property (T@"JFXDepthDataMediaReader",R,N) sharedDepthDataReader;
```

## Instance methods

```
-[JFXSharedMediaDataReaderManager playableElement];
-[JFXSharedMediaDataReaderManager initWithPlayableElement:];
-[JFXSharedMediaDataReaderManager setPlayableElement:];
-[JFXSharedMediaDataReaderManager setWeakSharedARMetadataReader:];
-[JFXSharedMediaDataReaderManager setWeakSharedDepthDataReader:];
-[JFXSharedMediaDataReaderManager sharedARMetadataReader];
-[JFXSharedMediaDataReaderManager sharedDepthDataReader];
-[JFXSharedMediaDataReaderManager weakSharedARMetadataReader];
-[JFXSharedMediaDataReaderManager weakSharedDepthDataReader];
```
