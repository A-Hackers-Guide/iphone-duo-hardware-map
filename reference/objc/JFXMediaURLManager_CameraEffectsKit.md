# `JFXMediaURLManager`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 2 instance methods, 19 class methods

## Instance variables

```
@"<JTFileURLSource>" _urlSource;
```

## Properties

```
@property (T@"<JTFileURLSource>",W,N,V_urlSource) urlSource;
```

## Class methods

```
+[JFXMediaURLManager sharedInstance];
+[JFXMediaURLManager ODRAssetsAreEmbedded];
+[JFXMediaURLManager videoExportURL:];
+[JFXMediaURLManager _audioRecordingURL:];
+[JFXMediaURLManager _capturedPhotoURL:isHEIF:];
+[JFXMediaURLManager _cleanupDirectory:];
+[JFXMediaURLManager _createDirectoryAtURL:error:];
+[JFXMediaURLManager _photoExportURL:isHEIF:];
+[JFXMediaURLManager _tempFileURLWithDirectory:file:error:];
+[JFXMediaURLManager _temporaryPhotoURL:fileName:];
+[JFXMediaURLManager _videoExportURL:];
+[JFXMediaURLManager audioRecordingURL:];
+[JFXMediaURLManager cachedExportFileURLWithError:];
+[JFXMediaURLManager capturedPhotoURL:isHEIF:];
+[JFXMediaURLManager cleanupTemporaryDirectories];
+[JFXMediaURLManager jfx_cleanupOldProjects];
+[JFXMediaURLManager photoExportURL:isHEIF:];
+[JFXMediaURLManager temporaryPhotoURL:fileName:];
+[JFXMediaURLManager videoRecordingFolderURL:];
```

## Instance methods

```
-[JFXMediaURLManager setUrlSource:];
-[JFXMediaURLManager urlSource];
```
