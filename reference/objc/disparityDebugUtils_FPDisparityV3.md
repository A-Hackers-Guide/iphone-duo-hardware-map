# `disparityDebugUtils`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 55 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
```

## Class methods

```
+[disparityDebugUtils createPathIfNeeded:];
```

## Instance methods

```
-[disparityDebugUtils initWithMetalContext:];
-[disparityDebugUtils saveF32Texture:AsF32BinaryFile:];
-[disparityDebugUtils saveRGBAF16PixelBuffer:out_width:out_height:AsPPMFileWithAlpha:];
-[disparityDebugUtils ApplyColorWheelAndWrite:height:data:fileFullPath:];
-[disparityDebugUtils saveF16Texture:AsF32BinaryFile:];
-[disparityDebugUtils saveRGB10A2PixelBuffer:out_width:out_height:AsPPMFileWithAlpha:];
-[disparityDebugUtils WriteBinDataToFile:length:fileFullPath:];
-[disparityDebugUtils computeRobustMinMaxForF16DisparityBuffer:WithDisparityScale:AndPercentile:OutSignalMin:OutSignalMax:];
-[disparityDebugUtils convertRGB10A2ToRGBA8:rbs:ToRGBA:outWidth:outHeight:];
-[disparityDebugUtils convertVUYA444:rbs:ToRGBA:ofSize:];
-[disparityDebugUtils makeCoherent:];
-[disparityDebugUtils save32BGRAPixelBuffer:AsPPMFile:];
-[disparityDebugUtils save420CVPixelBuffer:to:];
-[disparityDebugUtils saveAccumulationFrom:asBinaryFiles:forSize:costLineSize:];
-[disparityDebugUtils saveF16Buffer:AsPPMFile:scale:];
-[disparityDebugUtils saveF16DisparityBuffer:AsBinaryFile:];
-[disparityDebugUtils saveF16DisparityBuffer:AsGrayScalePPMFile:range:];
-[disparityDebugUtils saveF16DisparityBuffer:AsPPMFile:];
-[disparityDebugUtils saveF16DisparityBufferAsTurbo:AsPPMFile:WithDisparityScale:AndPercentile:];
-[disparityDebugUtils saveF16DisparityBufferAsTurbo:AsPPMFile:WithMin:WithMax:];
-[disparityDebugUtils saveF16DisparityTexture:AsBinaryFile:];
-[disparityDebugUtils saveF16DisparityTexture:AsPPMFile:];
-[disparityDebugUtils saveF16RGTexture:AsBinaryFile:];
-[disparityDebugUtils saveF16Texture:AsGrayScalePPMFile:range:];
-[disparityDebugUtils saveF16Texture:AsPPMFile:];
-[disparityDebugUtils saveF32Buffer:AsPPMFile:];
-[disparityDebugUtils saveF32DisparityBuffer:AsPPMFile:];
-[disparityDebugUtils saveF32FPBuffer:AsPPMFile:scale:];
-[disparityDebugUtils saveLumaTexture:to:];
-[disparityDebugUtils saveNCCOutputFrom:asBinaryFiles:];
-[disparityDebugUtils savePixelBuffer:AsBinaryFile:];
-[disparityDebugUtils saveRGB10A2PixelBuffer:AsPPMFile:];
-[disparityDebugUtils saveRGB10A2PixelBuffer:AsPPMFileWithAlpha:];
-[disparityDebugUtils saveRGB10A2PixelBuffer:out_width:out_height:AsPPMFile:];
-[disparityDebugUtils saveRGB10A2Texture:AsPPMFile:];
-[disparityDebugUtils saveRGBA16FTexture:AsF32File:];
-[disparityDebugUtils saveRGBA16FTexture:AsPPMFile:];
-[disparityDebugUtils saveRGBA8Texture:AsBinaryFile:];
-[disparityDebugUtils saveRGBA8Texture:AsPPMFile:];
-[disparityDebugUtils saveRGBAF16PixelBuffer:AsPPMFile:];
-[disparityDebugUtils saveRGBAF16PixelBuffer:AsPPMFileWithAlpha:];
-[disparityDebugUtils saveRGBAF16PixelBuffer:out_width:out_height:AsPPMFile:];
-[disparityDebugUtils saveRGBATexture:AsPPMFile:];
-[disparityDebugUtils saveRGF16ShiftmapTexture:AsPPMFileSx:AsPPMFileSy:];
-[disparityDebugUtils saveRGF16Texture:AsF32BinaryFile0:AsF32BinaryFile1:];
-[disparityDebugUtils saveRgbaF32PixelBuffer:AsPPMFile:];
-[disparityDebugUtils saveU16Texture:AsPGMFile:];
-[disparityDebugUtils saveU8Buffer:AsPPMFile:];
-[disparityDebugUtils saveU8Texture:AsPGMFile:];
-[disparityDebugUtils saveVUYA4444PixelBuffer:AsBinaryFile:];
-[disparityDebugUtils saveVUYA4444PixelBuffer:AsPPMFile:];
-[disparityDebugUtils saveVUYA4444PixelBuffer:out_width:out_height:AsBinaryFile:];
-[disparityDebugUtils saveVUYA4444PixelBuffer:out_width:out_height:AsPPMFile:];
-[disparityDebugUtils saveVUYA4444Texture:AsBinaryFile:];
-[disparityDebugUtils saveVUYA4444Texture:AsPPMFile:];
```
