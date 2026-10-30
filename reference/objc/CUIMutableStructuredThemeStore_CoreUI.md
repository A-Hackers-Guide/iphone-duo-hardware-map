# `CUIMutableStructuredThemeStore`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIStructuredThemeStore`
- 7 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSMutableDictionary" _memoryStore;
@"NSMutableDictionary" _nameIdentifierStore;
i _maxNameIdentifier;
@"NSMutableDictionary" _appearanceNameIdentifierStore;
i _maxAppearanceNameIdentifier;
@"NSMutableDictionary" _renditionInfoStore;
```

## Instance methods

```
-[CUIMutableStructuredThemeStore appearanceIdentifierForName:];
-[CUIMutableStructuredThemeStore imagesWithName:];
-[CUIMutableStructuredThemeStore deploymentPlatform];
-[CUIMutableStructuredThemeStore maximumRenditionKeyTokenCount];
-[CUIMutableStructuredThemeStore renditionKeyForName:];
-[CUIMutableStructuredThemeStore dealloc];
-[CUIMutableStructuredThemeStore _removeRenditionInfoForImageWithName:];
-[CUIMutableStructuredThemeStore keyFormat];
-[CUIMutableStructuredThemeStore themeStore];
-[CUIMutableStructuredThemeStore renditionKeyForAssetWithName:withDescription:];
-[CUIMutableStructuredThemeStore clearRenditionCache];
-[CUIMutableStructuredThemeStore renditionWithKey:usingKeySignature:];
-[CUIMutableStructuredThemeStore insertCGImage:withName:andDescription:];
-[CUIMutableStructuredThemeStore allImageNames];
-[CUIMutableStructuredThemeStore appearances];
-[CUIMutableStructuredThemeStore removeImageNamed:withDescription:];
-[CUIMutableStructuredThemeStore removeImagesNamed:];
-[CUIMutableStructuredThemeStore _addRenditionInfoForImageWithName:andKey:];
-[CUIMutableStructuredThemeStore renditionInfoForIdentifier:];
-[CUIMutableStructuredThemeStore defaultAppearanceName];
-[CUIMutableStructuredThemeStore nameForAppearanceIdentifier:];
-[CUIMutableStructuredThemeStore usesCUISystemThemeRenditionKey];
-[CUIMutableStructuredThemeStore renditionWithKey:];
-[CUIMutableStructuredThemeStore initWithIdentifier:];
-[CUIMutableStructuredThemeStore deploymentPlatformString];
-[CUIMutableStructuredThemeStore canGetRenditionWithKey:];
-[CUIMutableStructuredThemeStore renditionKeyForName:cursorHotSpot:];
-[CUIMutableStructuredThemeStore path];
```
