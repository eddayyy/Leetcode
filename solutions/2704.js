/**
 * @param {string} val
 * @return {Object}
 */
// var expect = function(val) {
//     return {
//         toBe: (val2) => {
//             if (val === val2) {
//                 return true;
//             }
//             throw "Not Equal";
//         },
//         notToBe: (val2) => {
//             if (val !== val2){
//                 return true;
//             }
//             throw "Equal";
//         }
//     }
// };

class Expect {
  constructor(val) {
    this.val = val;
  }

  toBe(val2) {
    if (this.val === val2) {
      return true;
    }
    throw "Not Equal";
  }

  notToBe(val2) {
    if (this.val !== val2) {
      return true;
    }
    throw "Equal";
  }
}

var expect = function (val) {
  return new Expect(val);
};
/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
