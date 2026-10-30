# `SBFWallpaperCoreAnalyticsLogger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"PBUIWallpaperDefaultsDomain" _wallpaperDefaultsDomain;
@"NSString" _homeType;
@"NSString" _lockType;
@"NSString" _homeName;
@"NSString" _lockName;
B _irisEnabled;
B _sharedWallpaper;
Q _ageOfWallpaper;
```

## Properties

```
@property (TQ,N,V_ageOfWallpaper) ageOfWallpaper;
```

## Instance methods

```
-[SBFWallpaperCoreAnalyticsLogger init];
-[SBFWallpaperCoreAnalyticsLogger ageOfWallpaper];
-[SBFWallpaperCoreAnalyticsLogger initWithWallpaperDefaultsDomain:];
-[SBFWallpaperCoreAnalyticsLogger saveStateOfWallpaperToCoreAnalytics:withHasVideo:hasProcedural:name:];
-[SBFWallpaperCoreAnalyticsLogger sendStateOfWallpaperToCoreAnalytics];
-[SBFWallpaperCoreAnalyticsLogger setAgeOfWallpaper:];
```
