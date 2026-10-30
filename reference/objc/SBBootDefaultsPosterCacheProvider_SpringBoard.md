# `SBBootDefaultsPosterCacheProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PRSPosterConfigurationCacheProviding`
- 1 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBBootDefaults" _bootDefaults;
```

## Properties

```
@property (T@"NSData",&,N) lastActiveLockPoster;
@property (T@"NSData",&,N) lastActiveHomePoster;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBootDefaultsPosterCacheProvider init];
-[SBBootDefaultsPosterCacheProvider lastActiveHomePoster];
-[SBBootDefaultsPosterCacheProvider lastActiveLockPoster];
-[SBBootDefaultsPosterCacheProvider setLastActiveHomePoster:];
-[SBBootDefaultsPosterCacheProvider setLastActiveLockPoster:];
```
