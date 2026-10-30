# `AVFragmentedMovieMinder`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVFragmentedAssetMinder`
- 0 instance variables, 2 properties, 7 instance methods, 1 class methods

## Properties

```
@property (Td,N) mindingInterval;
@property (T@"NSArray",R,N) movies;
```

## Class methods

```
+[AVFragmentedMovieMinder fragmentedMovieMinderWithMovie:mindingInterval:];
```

## Instance methods

```
-[AVFragmentedMovieMinder mindingInterval];
-[AVFragmentedMovieMinder _throwsWhenAlreadyMindedAssetIsAdded];
-[AVFragmentedMovieMinder addFragmentedMovie:];
-[AVFragmentedMovieMinder initWithMovie:mindingInterval:];
-[AVFragmentedMovieMinder movies];
-[AVFragmentedMovieMinder removeFragmentedMovie:];
-[AVFragmentedMovieMinder setMindingInterval:];
```
