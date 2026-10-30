# `SBCollectionViewCell`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _performSetHighlighted;
B _protectDelayedUnhighlights;
@"<SBCollectionViewCellDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBCollectionViewCellDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_protectDelayedUnhighlights) protectDelayedUnhighlights;
```

## Instance methods

```
-[SBCollectionViewCell setDelegate:];
-[SBCollectionViewCell setHighlighted:];
-[SBCollectionViewCell prepareForReuse];
-[SBCollectionViewCell delegate];
-[SBCollectionViewCell _didSetHighlighted:];
-[SBCollectionViewCell _performSetHighlighted];
-[SBCollectionViewCell protectDelayedUnhighlights];
-[SBCollectionViewCell setHighlighted:afterDelay:];
-[SBCollectionViewCell setProtectDelayedUnhighlights:];
```
