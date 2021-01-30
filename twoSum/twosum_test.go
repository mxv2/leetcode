package twoSum

import (
	"math/rand"
	"reflect"
	"testing"
	"time"
)

type args struct {
	nums   []int
	target int
}

var tests = []struct {
	name string
	args args
	want []int
}{
	{
		name: "Example 1",
		args: args{
			nums:   []int{2, 7, 11, 15},
			target: 9,
		},
		want: []int{0, 1},
	},
	{
		name: "Example 2",
		args: args{
			nums:   []int{3, 2, 4},
			target: 6,
		},
		want: []int{1, 2},
	},
	{
		name: "Example 3",
		args: args{
			nums:   []int{3, 3},
			target: 6,
		},
		want: []int{0, 1},
	},
	{
		name: "Example 4: Missing solution",
		args: args{
			nums:   []int{2, 7, 11, 15},
			target: 6,
		},
		want: []int{},
	},
}

func Test_twoSum(t *testing.T) {
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := twoSum(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

var benchmarks = []struct {
	name string
	args args
	want []int
}{
	{
		name: "Benchmark 1",
		args: args{
			nums:   []int{},
			target: 9,
		},
	},
	{
		name: "Benchmark 2",
		args: args{
			nums:   []int{},
			target: 9,
		},
	},
}

func genBenchmarks() {
	rand.Seed(time.Now().Unix())

	tt1 := &benchmarks[0]
	len1 := 100
	tt1.args.nums = make([]int, len1)
	tt1.args.nums[len1-2] = 2
	tt1.args.nums[len1-1] = 7
	for i := 0; i < len1-2; i++ {
		tt1.args.nums[i] = rand.Intn(2000000000) - 1000000000
	}

	tt2 := &benchmarks[0]
	len2 := 1000
	tt2.args.nums = make([]int, len2)
	tt2.args.nums[len2-2] = 2
	tt2.args.nums[len2-1] = 7
	for i := 1; i < len2-2; i++ {
		tt2.args.nums[i] = rand.Intn(2000000000) - 1000000000
	}
}

func init() {
	genBenchmarks()
}

func Benchmark_twoSum_BruteForce_100(b *testing.B) {
	b.ResetTimer()

	tt := benchmarks[0]
	for i := 0; i < b.N; i++ {
		twoSum(tt.args.nums, tt.args.target)
	}
}

func Benchmark_twoSum_BruteForce_1000(b *testing.B) {
	b.ResetTimer()

	tt := benchmarks[1]
	for i := 0; i < b.N; i++ {
		twoSum(tt.args.nums, tt.args.target)
	}
}

func Benchmark_twoSum_Hash_100(b *testing.B) {
	b.ResetTimer()

	tt := benchmarks[0]
	for i := 0; i < b.N; i++ {
		twoSumHash(tt.args.nums, tt.args.target)
	}
}

func Benchmark_twoSum_Hash_1000(b *testing.B) {
	b.ResetTimer()

	tt := benchmarks[1]
	for i := 0; i < b.N; i++ {
		twoSumHash(tt.args.nums, tt.args.target)
	}
}

func Benchmark_twoSum_HashOnePass_100(b *testing.B) {
	b.ResetTimer()

	tt := benchmarks[0]
	for i := 0; i < b.N; i++ {
		twoSumHashOnePass(tt.args.nums, tt.args.target)
	}
}

func Benchmark_twoSum_HashOnePass_1000(b *testing.B) {
	b.ResetTimer()

	tt := benchmarks[1]
	for i := 0; i < b.N; i++ {
		twoSumHashOnePass(tt.args.nums, tt.args.target)
	}
}
