# `NSDiffableDataSourceSectionTransaction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@ _sectionIdentifier;
@"NSDiffableDataSourceSectionSnapshot" _initialSnapshot;
@"NSDiffableDataSourceSectionSnapshot" _finalSnapshot;
@"NSOrderedCollectionDifference" _difference;
```

## Properties

```
@property (T@,R,N,V_sectionIdentifier) sectionIdentifier;
@property (T@"NSDiffableDataSourceSectionSnapshot",R,N,V_initialSnapshot) initialSnapshot;
@property (T@"NSDiffableDataSourceSectionSnapshot",R,N,V_finalSnapshot) finalSnapshot;
@property (T@"NSOrderedCollectionDifference",R,N,V_difference) difference;
```

## Instance methods

```
-[NSDiffableDataSourceSectionTransaction _spiCopy];
-[NSDiffableDataSourceSectionTransaction finalSnapshot];
-[NSDiffableDataSourceSectionTransaction description];
-[NSDiffableDataSourceSectionTransaction sectionIdentifier];
-[NSDiffableDataSourceSectionTransaction difference];
-[NSDiffableDataSourceSectionTransaction initialSnapshot];
-[NSDiffableDataSourceSectionTransaction isEqual:];
-[NSDiffableDataSourceSectionTransaction initWithSectionIdentifier:initialSnapshot:finalSnapshot:difference:];
```
