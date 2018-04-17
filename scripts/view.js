window.view = function() {
  // Render each object.
  for (var x = 0; x < this.objects.length; ++x) {

    // Calculate Y coordinate.
    if (thisObject.verticalVelocity) {
      var newY = thisObject.y + thisObject.verticalVelocity;
      if (newY <= 0) {
        thisObject.set('falling', false);
        thisObject.set('verticalVelocity', 0);
        thisObject.set('y', 0);
      }
      else {
        thisObject.set('falling', true);
        thisObject.set('y', newY);

        // Collision detection: Y
        if (thisObject.collisionY) {
          for (var y = 0; y < this.objects.length; ++y) {
            var thatObject = this.objects[y];
            if (
              x === y ||
              !thatObject ||
              thatObject.static ||
              !thisObject.isInside(thatObject)
            ) {
              continue;
            }
            thisObject.collisionY(thatObject);
          }
        }
      }
    }

    // Calculate X coordinate.
    if (thisObject.horizontalVelocity) {
      thisObject.set('x', thisObject.x + thisObject.horizontalVelocity);

      // Collision detection: X
      if (thisObject.collisionX) {
        for (var y = 0; y < this.objects.length; ++y) {
          var thatObject = this.objects[y];
          if (
            x === y ||
            !thatObject ||
            thatObject.static ||
            !thisObject.isInside(thatObject)
          ) {
            continue;
          }
          thisObject.collisionX(thatObject);
        }
      }
    }

    if (thisObject.controller) {
      thisObject.controller();
    }
    thisObject.view();
  }

  // 60 FPS
  setTimeout(
    window.view,
    Math.max(0, 17 - new Date().getTime() + this.lastRender)
  );
}.bind(window.model);
