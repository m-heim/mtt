use clap::Parser;

/// Search for a pattern in a file and display the lines that contain it.
#[derive(Parser)]
struct Cli {
    /// The subcommand
    command: String,
    debug: bool,
}

fn main() {
    println!("Thanks for using mtt! :)");
    let args = Cli::parse();
}
